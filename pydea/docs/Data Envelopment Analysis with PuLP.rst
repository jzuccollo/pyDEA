Data envelopment analysis using PuLP
====================================

DEA is most useful when a comparison is sought against “best practices”
where the analyst doesn’t want the frequency of poorly run operations to
affect the analysis. DEA has been applied in many situations such as:
health care (hospitals, doctors), education (schools, universities),
banks, manufacturing, benchmarking, management evaluation, fast food
restaurants, and retail stores. The analyzed data sets vary in size.
Some analysts work on problems with as few as 15 or 20 DMUs while others
are tackling problems with over 10,000 DMUs.

`Strengths and limitations <http://mat.gsia.cmu.edu/classes/QUANT/NOTES/chap12.pdf>`__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As the earlier list of applications suggests, DEA can be a powerful tool
when used wisely. A few of the characteristics that make it powerful
are: - DEA can handle multiple input and multiple output models. - It
doesn’t require an assumption of a functional form relating inputs to
outputs. - DMUs are directly compared against a peer or combination of
peers. - Inputs and outputs can have very different units. For example,
X1 could be in units of lives saved and X2 could be in units of dollars
without requiring an a priori tradeof between the two.

The same characteristics that make DEA a powerful tool can also create
problems. An analyst should keep these limitations in mind when choosing
whether or not to use DEA. - Since DEA is an extreme point technique,
noise (even symmetrical noise with zero mean) such as measurement error
can cause significant problems. - DEA is good at estimating “relative”
efficiency of a DMU but it converges very slowly to “absolute”
efficiency. In other words, it can tell you how well you are doing
compared to your peers but not compared to a “theoretical maximum.” -
Since DEA is a nonparametric technique, statistical hypothesis tests are
difficult and are the focus of ongoing research. - Since a standard
formulation of DEA creates a separate linear program for each DMU, large
problems can be computationally intensive.

References
~~~~~~~~~~

-  `Tim Coelli’s summary of productivity
   measurement <http://facweb.knowlton.ohio-state.edu/pviton/courses/crp394/coelli_Intro_effic.pdf>`__
-  `PuLP <http://www.coin-or.org/PuLP/pulp.html>`__
-  `Python classes
   docs <https://docs.python.org/2/tutorial/classes.html>`__ and `hints
   for class
   design <http://stackoverflow.com/questions/4203163/how-do-i-design-a-class-in-python>`__
-  `Weight restrictions in
   DEA <http://www.wbs.ac.uk/downloads/working_papers/352.pdf>`__
-  `Overview of
   DEA <http://www.nhh.no/Files/Filer/institutter/for/seminars/accounting_management_science/2007_spring/300507.pdf>`__
-  `NZ Post
   example <https://secure.orsnz.org.nz/conf45/program/Papers/ORSNZ2010_Priddey.pdf>`__
-  `Non-discretionary inputs in
   healthcare <http://papers.ssrn.com/sol3/papers.cfm?abstract_id=952629>`__
-  `Non-discretionary
   inputs <https://www.nhh.no/Admin/Public/Download.aspx?file=Files%2FFiler%2Finstitutter%2Ffor%2Fseminars%2Faccounting_management_science%2F2007_spring%2F300507-1.pdf>`__
-  `DEA conference
   proceedings <http://deazone.com/en/wp-content/uploads/2014/05/DEA2013-Proceedings.pdf>`__
-  `DEAP programme
   notes <http://www.owlnet.rice.edu/~econ380/DEAP.PDF>`__
-  `DEA on panel
   data <http://competitionpolicy.ac.uk/documents/107435/107587/1.114399!ccp09-6.pdf>`__
-  `Data preparation for
   DEA <www.clarku.edu/~jsarkis/sarkischapter.doc>`__
-  `Methods for increasing
   discrimination <http://www.uff.br/decisao/annals_angulomeza-lins.pdf>`__
-  `When and how to use
   PCA-DEA <http://pluto.huji.ac.il/~msnic/PCA&DEA.pdf>`__

The linear programming problem
==============================

pyDEA currently solves an input-oriented DEA model using PuLP’s linear
programme solver.

.. code:: latex

    %%latex
    An input-oriented DEA model with constant returns to scale is solved with the following LP model:
    
    \begin{equation}
    \max e_{j_0} = \sum_r u_r y_{rj_0} - \mu_0
    \end{equation}
    
    subject to
    
    \begin{aligned}
    \sum_i v_i x_{ij_0} &= 1 \\
    \sum_r u_r y_{rj} - \sum_i v_i x_{ij} - \mu_0 &\leq 0, \quad j \in 1, 2, \ldots, n \\
    u_r, v_i &\geq \varepsilon
    \end{aligned}
    
    where
    
    \begin{aligned}
    x_{ij} &= \mbox{quantity of input } i \mbox{ for unit } j \\
    v_{i} &= \mbox{weight attached to input } i \\
    y_{ij} &= \mbox{quantity of output } r \mbox{ for unit } j \\
    u_{i} &= \mbox{weight attached to output } r \\
    e_{j_0} &= \mbox{efficiency score} \\
    \mu_0 &= \mbox{VRS parameter} \\
    j_0 &= \mbox{DMU under analysis} \\
    \end{aligned}
    
    Input and output quantities are fixed by the data, weights are the decision variables and the efficiency score is the output.



.. math::

    An input-oriented DEA model with constant returns to scale is solved with the following LP model:
    
    \begin{equation}
    \max e_{j_0} = \sum_r u_r y_{rj_0} - \mu_0
    \end{equation}
    
    subject to
    
    \begin{aligned}
    \sum_i v_i x_{ij_0} &= 1 \\
    \sum_r u_r y_{rj} - \sum_i v_i x_{ij} - \mu_0 &\leq 0, \quad j \in 1, 2, \ldots, n \\
    u_r, v_i &\geq \varepsilon
    \end{aligned}
    
    where
    
    \begin{aligned}
    x_{ij} &= \mbox{quantity of input } i \mbox{ for unit } j \\
    v_{i} &= \mbox{weight attached to input } i \\
    y_{ij} &= \mbox{quantity of output } r \mbox{ for unit } j \\
    u_{i} &= \mbox{weight attached to output } r \\
    e_{j_0} &= \mbox{efficiency score} \\
    \mu_0 &= \mbox{VRS parameter} \\
    j_0 &= \mbox{DMU under analysis} \\
    \end{aligned}
    
    Input and output quantities are fixed by the data, weights are the decision variables and the efficiency score is the output.



