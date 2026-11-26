
import pandas as pd

df = pd.DataFrame({
    "employee": ["Alice", "Bob", "Charlie", "Diana","Sreeni","Suresh","Sudhakar","Alex","Bob","Queen"],
    "department": ["Sales", "Sales", "IT", "IT","Engg","Engg","Engg","Sales","IT","IT"],
    "salary": [60000, 80000, 100000, 120000,180000,200000,239000,230000,190000,230000]
})

# apply() — Applies a function along an axis
df['bonus'] = df.apply(lambda row:row['salary']*0.15 if row['department'] == 'Engg' else row['salary']*0.10, axis=1)
print('apply()')
print(df)

dept_codes = {"Sales": "SLS", "IT": "TECH", "Engg": "ENG"}
df["dept_code"] = df["department"].map(dept_codes)
print('map()')
print(df)

print('Replace',df.replace({'Engg':'Engineering','IT':'Information Technology'}))

print('Pivoted')
print(df.pivot(index='employee',columns='department',values='salary'))

print('Pivot_table')
print(df.pivot_table(index='department',values='salary',aggfunc=['mean', 'count']))

# First create a second numeric column so we have two value columns to melt
df_wide = df[["employee", "salary"]].copy()
df_wide["bonus"] = df["salary"] * 0.10

melted = df_wide.melt(id_vars=["employee"], value_vars=["salary", "bonus"],
                      var_name="pay_type", value_name="amount")
print(melted)

df_skills = df[["employee", "department"]].head(2).copy()
df_skills["skills"] = [["CRM", "Negotiation"], ["Cold Calling", "CRM"]]

exploded = df_skills.explode("skills")
print(exploded)

df["overall_rank"] = df["salary"].rank(ascending=False)
df["dept_rank"] = df.groupby("department")["salary"].rank(ascending=False)
print(df)

df["rolling_2_avg"] = df["salary"].rolling(window=2).mean()

print(df)

