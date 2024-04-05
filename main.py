import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a dataframe
df = pd.read_csv('waze_dataset.csv')

# Box plot
plt.figure(figsize=(5,1))
sns.boxplot(x=df['sessions'], fliersize=1)
plt.title('sessions box plot')

# Histogram
plt.figure(figsize=(5,3))
sns.histplot(x=df['sessions'])
median = df['sessions'].median()
plt.axvline(median, color='red', linestyle='--')
plt.text(75,1200, f'median={median:.1f}', color='red')
plt.title('sessions histogram')

# Box plot
plt.figure(figsize=(5,1))
sns.boxplot(x=df['drives'], fliersize=1)
plt.title('drives box plot')

# Helper function to plot histograms
def histogrammer(column_str, **kwargs):
    median = round(df[column_str].median(), 1)
    plt.figure(figsize=(5,3))
    ax = sns.histplot(x=df[column_str], **kwargs)
    plt.axvline(median, color='red', linestyle='--')
    ax.text(0.25, 0.85, f'median={median}', color='red', ha='left', va='top', transform=ax.transAxes)
    plt.title(f'{column_str} histogram')

# Histogram
histogrammer('drives')

# Pie chart
fig = plt.figure(figsize=(3,3))
data = df['device'].value_counts()
plt.pie(data, labels=[f'{data.index[0]}: {data.values[0]}', f'{data.index[1]}: {data.values[1]}'], autopct='%1.1f%%')
plt.title('Users by device')

# Scatter plot
sns.scatterplot(data=df, x='driving_days', y='activity_days')
plt.title('driving_days vs. activity_days')
plt.plot([0,31], [0,31], color='red', linestyle='--')

# Create `km_per_driving_day` column
df['km_per_driving_day'] = df['driven_km_drives'] / df['driving_days']

# Histogram
plt.figure(figsize=(12,5))
sns.histplot(data=df, x='km_per_driving_day', bins=range(0,1201,20), hue='label', multiple='fill')
plt.ylabel('%', rotation=0)
plt.title('Churn rate by mean km per driving day')

# Histogram
plt.figure(figsize=(12,5))
sns.histplot(data=df, x='driving_days', bins=range(1,32), hue='label', multiple='fill', discrete=True)
plt.ylabel('%', rotation=0)
plt.title('Churn rate per driving day')

# Calculate `percent_sessions_in_last_month`
df['percent_sessions_in_last_month'] = df['sessions'] / df['total_sessions']
df['percent_sessions_in_last_month'].median()

# Histogram
histogrammer('percent_sessions_in_last_month', hue=df['label'], multiple='layer', median_text=False)

# Outlier imputation
def outlier_imputer(column_name, percentile):
    threshold = df[column_name].quantile(percentile)
    df.loc[df[column_name] > threshold, column_name] = threshold
    print(f'{column_name:>25} | percentile: {percentile} | threshold: {threshold}')

for column in ['sessions', 'drives', 'total_sessions', 'driven_km_drives', 'duration_minutes_drives']:
    outlier_imputer(column, 0.95)

# Calculate `monthly_drives_per_session_ratio`
df['monthly_drives_per_session_ratio'] = df['drives'] / df['sessions']
