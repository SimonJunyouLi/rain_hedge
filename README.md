# Rain Hedge
Hedging implementation to bound errors in rain probability prediction. 

## Problem Statement

The first line of the input contains two integers $N$ and $T ~{} (1 \leq N \leq 10, 100 \leq T \leq 1000)$, the number of models used by SwissMeteo and the number of days for which you have to predict the weather.

For the next $T$ timesteps, the predictions of the $N$ models will appear in the input as a line of N integers $x^{(t)}$. Each $x^{(t)}$ will be in $\{0, 1\}$, with 1 meaning that the i-th model predicts that it will rain. Your solution has to output a number $p^{(t)} \in \[0, 1\]$ which is your estimate of the probability that it will rain.

After you have printed your estimate $p^{(t)}$, the real outcome will be available in the input as a new line with one integer $y^{(t)} \in \\{ 0, 1 \\}$. The cost incurred by your decision on this timestep will be $|p^{(t)} − y^{(t)}|$. When you have read the real outcome, the predictions of the new day will be available in the input. Your program should terminate after T timesteps.

The solution's total cost is at most 100 more than the cost of the best expert, that is

```math
\begin{align*}
\sum^{T}_{t=1}|p^{(t)} - y^{(t)} \leq 100 + \min_{j \in [N]} \sum^{T}_{t=1}|x_j^{(t)} - y^{(t)}|
\end{align*}
```