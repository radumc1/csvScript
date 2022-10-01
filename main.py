import pandas as pd

customers = pd.read_excel("1_bunx3.xlsx")
calls = pd.read_excel("2_bun.xlsx")
outer_join_df = customers.merge(calls, how="outer", on="Parcela")
outer_join_df.to_excel("OuterJoin.xlsx")
