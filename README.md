# genpark-matrix-profile-discord-anomaly-detector-skill

Agent Skill implementing the **Matrix Profile 1-NN Subsequence Distance Engine** for time-series discord anomaly discovery and motif detection without false positive trivial matches.

## Architectural Overview
```mermaid
flowchart TD
    Series["Time Series (Length n)"] --> Slide["Sliding Window Subsequences (Length m)"]
    Slide --> Exclude["Exclusion Zone: |i - j| >= m // 2"]
    Exclude --> Nearest["Find 1-Nearest Neighbor Euclidean Distance for Each Window"]
    Nearest --> Profile["Construct Matrix Profile Array MP[i]"]
    Profile --> Max["Argmax(MP): Top Discord Anomaly Subsequence"]
```
