from client import MatrixProfileDetector

ts = [1, 2, 1, 2, 1, 2, 10, 20, 1, 2, 1, 2]
res = MatrixProfileDetector.compute_matrix_profile(ts, subseq_len=3)

print("Matrix Profile Anomaly Detection:")
print(f"Top Discord Index: {res['top_discord_index']}")
print(f"Top Discord Distance: {res['top_discord_distance']:.2f}")
print(f"Discord Subsequence: {res['discord_subsequence']}")
