# from typing import List, Dict
# from 0-stream_users import stream_users
#
#
# def stream_users_in_batches(batch_size: int):
#     """
#     Generator that yields batches of users from the stream_users generator
#     """
#     batch: List[Dict] = []
#     for user in stream_users():  # 1 loop
#         batch.append(user)
#         if len(batch) == batch_size:
#             yield batch
#             batch = []
#     if batch:  # yield last incomplete batch
#         yield batch
#
#
# def batch_processing(batch_size: int):
#     """
#     Process batches and filter users over the age of 25
#     """
#     for batch in stream_users_in_batches(batch_size):  # 2nd loop
#         for user in batch:  # 3rd loop
#             if user["age"] > 25:
#                 print(user)
