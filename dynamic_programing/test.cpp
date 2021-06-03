#include <bits/stdc++.h>
using namespace std;

int main()
{
  int n, x;
  cin >> n >> x;
  int hrr[n], srr[n];
  for (int i = 0; i < n; i++)
    cin >> hrr[i];
  for (int i = 0; i < n; i++)
    cin >> srr[i];

  int dp[n + 1][x + 1];

  for (int i = 0; i <= n; i++)
  {
    for (int j = 0; j <= x; j++)
    {
      dp[i][j] = 0;
      if (i !=0 and j != 0)
      {

        if (j < hrr[i - 1])
          dp[i][j] = dp[i - 1][j];
        else
          dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - hrr[i - 1]] + srr[i - 1]);
      }
    }
  }
  cout << dp[n][x] << endl;
}