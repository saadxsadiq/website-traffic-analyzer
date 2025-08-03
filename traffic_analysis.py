
import pandas as pd

print("🌐 WEBSITE TRAFFIC ANALYZER")
print("=" * 30)

# Load the data
df = pd.read_csv('website_traffic_analysis.csv')

print(f"✅ Loaded {len(df)} days of traffic data")

# Basic metrics
total_views = df['page_views'].sum()
total_visitors = df['unique_visitors'].sum()
avg_bounce_rate = df['bounce_rate'].mean()
avg_conversion = df['conversion_rate'].mean()

print(f"\n📊 TRAFFIC METRICS:")
print(f"   • Total Page Views: {total_views:,}")
print(f"   • Total Visitors: {total_visitors:,}")
print(f"   • Average Bounce Rate: {avg_bounce_rate:.1%}")
print(f"   • Average Conversion Rate: {avg_conversion:.1%}")

# Traffic sources analysis
source_performance = df.groupby('source')['page_views'].sum().sort_values(ascending=False)

print(f"\n🎯 TRAFFIC SOURCES:")
for source, views in source_performance.items():
    percentage = (views / total_views) * 100
    print(f"   • {source}: {views:,} views ({percentage:.1f}%)")

# Best performing days
df['date'] = pd.to_datetime(df['date'])
best_day = df.loc[df['page_views'].idxmax()]

print(f"\n🏆 BEST PERFORMANCE:")
print(f"   • Best Day: {best_day['date'].strftime('%Y-%m-%d')}")
print(f"   • Views: {best_day['page_views']:,}")
print(f"   • Conversion: {best_day['conversion_rate']:.1%}")

print(f"\n📈 RECOMMENDATIONS:")
print(f"   • Focus marketing on {source_performance.index[0]} (top source)")
print(f"   • Improve bounce rate (currently {avg_bounce_rate:.1%})")
print(f"   • Optimize for conversion (currently {avg_conversion:.1%})")

print(f"\n✅ Analysis Complete! Traffic insights ready.")
