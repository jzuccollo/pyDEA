import numpy as np
import pulp


class DEA:
    """
    A container for the elements of a data envelopment analysis problem. Sets up the linear programmes and solves them with pulp.
    
    Requires:
    
        inputs: a numpy array of the inputs to the DMUs
        outputs: a numpy array of the outputs from the DMUs
        kind: 'VRS' or 'CRS'    
    """
    def __init__(self, inputs, outputs, kind='CRS'):
        self.inputs = inputs
        self.outputs = outputs
        self.returns = kind
               
        self.J, self.I = self.inputs.shape  # no of firms, inputs
        self.R = self.outputs.shape[1]  # no of outputs
        self._i = np.arange(self.I)  # inputs
        self._r = np.arange(self.R)  # outputs
        self._j = np.arange(self.J)  # DMUs
        
        assert self.inputs.shape[0] == self.outputs.shape[0]  # check the inputs and outputs have the same number of DMUs
        
        self.dmus = self._create_problems()  # creates dictionary of pulp.LpProblem objects for the DMUs

    def _create_problems(self):
        dmu_dict = {}
        for j0 in np.arange(self.inputs.shape[0]):
            dmu_dict[j0] = self._make_problem(self.inputs, self.outputs, j0, self.returns)
        return dmu_dict
    
    def _make_problem(self, inputs, outputs, j0, returns):
        ##Set up pulp
        prob = pulp.LpProblem("DMU_"+str(j0), pulp.LpMaximize)
        self.inputWeights = pulp.LpVariable.dicts("inputWeight", (self._j, self._i), lowBound=0)
        self.outputWeights = pulp.LpVariable.dicts("outputWeight", (self._j, self._r), lowBound=0)
                
        ##Set returns to scale
        if returns == "CRS":
            w = 0
        elif returns == "VRS":
            w = pulp.LpVariable.dicts("w", (self._j, self._r))
        else:
            raise Exception(ValueError)

        ##Set up objective function
        prob += sum([self.outputs[j0][r1] * self.outputWeights[j0][r1] for r1 in self._r]) - w

        ##Set up constraints
        prob += sum([self.inputs[j0][i1] * self.inputWeights[j0][i1] for i1 in self._i]) == 1, "Norm_constraint"
        for j1 in self._j:
            prob += self._dmu_constraint(j0, j1, self._i, self._r)  - w <= 0, "DMU_constraint_" + str(j1)
        return prob
    
    def _dmu_constraint(self, j0, j1, i, r):
        eOut = sum([self.outputs[j1][r1] * self.outputWeights[j0][r1] for r1 in r])
        eIn = sum([self.inputs[j1][i1] * self.inputWeights[j0][i1] for i1 in i])
        return eOut - eIn     

    def solve(self):
        self.status = {}
        self.weights = {}
        self.efficiency = {}
        for ind, problem in self.dmus.iteritems():
            problem.solve()
            self.status[ind] = pulp.LpStatus[problem.status]
            self.weights[ind] = {}
            for v in problem.variables():
                self.weights[ind][v.name] = v.varValue
            self.efficiency[ind] = pulp.value(problem.objective)