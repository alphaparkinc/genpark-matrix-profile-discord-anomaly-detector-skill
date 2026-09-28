"""Matrix Profile Discord Anomaly Detection Engine.
100% Python Standard Library.
"""

import math

class MatrixProfileDetector:
    """Matrix Profile 1D Euclidean distance profile for discord anomaly detection."""
    @staticmethod
    def compute_matrix_profile(series, subseq_len=4):
        n = len(series)
        m = subseq_len
        num_subseq = n - m + 1
        assert num_subseq >= 2, "Series too short"

        mp = [float("inf")] * num_subseq
        mp_idx = [-1] * num_subseq
        subseqs = [series[i : i + m] for i in range(num_subseq)]

        for i in range(num_subseq):
            best_dist = float("inf")
            best_j = -1
            sub_i = subseqs[i]
            for j in range(num_subseq):
                if abs(i - j) < m // 2:
                    continue
                sub_j = subseqs[j]
                d = math.sqrt(sum((a - b)**2 for a, b in zip(sub_i, sub_j)))
                if d < best_dist:
                    best_dist = d
                    best_j = j
            mp[i] = best_dist
            mp_idx[i] = best_j

        max_dist = max(mp)
        discord_idx = mp.index(max_dist)
        return {
            "matrix_profile": mp,
            "profile_indices": mp_idx,
            "top_discord_index": discord_idx,
            "top_discord_distance": max_dist,
            "discord_subsequence": subseqs[discord_idx]
        }
