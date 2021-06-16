\ifndef{neuripsExperimentResults}
\define{neuripsExperimentResults}

\editme

\subsection{NeurIPS Experiment Results}

\notes{The final results of the experiment were as follows. From 170 papers 4 had to be withdrawn or were rejected without completing the review process, for the remainder, the 'confusion matrix' for the two committee's decisions is below.}

<table>
  <tr>
  <td colspan="2"></td><td colspan="2">Committee 1</td>
  </tr>
  <tr>
  <td colspan="2"></td><td>Accept</td><td>Reject</td>
  </tr>
  <tr>
    <td rowspan="2">Committee 2</td><td>Accept</td><td>22</td><td>22</td>
  </tr>
  <tr>
    <td>Reject</td><td>21</td><td>101</td>
  </tr>
</table>

4 papers rejected or withdrawn without review.

\notes{\subsection{Summarizing the Table}}

\notes{There are a few ways of summarizing the numbers in this table as percent or probabilities. First of all, the inconsistency, the proportion of decisions that were not the same across the two committees. The decisions were inconsistent for 43 out of 166 papers or 0.259 as a proportion. This number is perhaps a natural way of summarizing the figures if you are submitting your paper and wish to know an estimate of what the probability is that your paper would have different decisons according to the different committes. Secondly, the accept precision: if you are attending the conference and looking at any given paper, then you might want to know the probability that the paper would have been rejected in an independent rerunning of the conference. We can estimate this for Committee 1's conference as 22/(22 + 22) = 0.5 (50%) and for Committee 2's conference as 21/(22+21) = 0.49 (49%). Averaging the two estimates gives us 49.5%. Finally, the reject precision: if your paper was rejected from the conference, you might like an estimate of the probability that the same paper would be rejected again if the review process had been independently rerun. That estimate is 101/(22+101) = 0.82 (82%) for Committee 1 and 101/(21+101)=0.83 (83%) for Committee 2, or on average 82.5%. A final quality estimate might be the ratio of consistent accepts to consistent rejects, or the agreed accept rate, 22/123 = 0.18 (18%).}

\notes{* *inconsistency*: 43/166 = **0.259**
    * proportion of decisions that were not the same
* *accept precision* $0.5 \times 22/44$ + $0.5 \times 21/43$ = **0.495**
    * probability any accepted paper would be rejected in a rerunning
* *reject precision* = $0.5\times 101/(22+101)$ + $0.5\times 101/(21 + 101)$ = **0.175**
    * probability any rejected paper would be rejected in a rerunning
* *agreed accept rate* = 22/101 = **0.218**
* ratio between aggreed accepted papers and agreed rejected papers.}

\endif
