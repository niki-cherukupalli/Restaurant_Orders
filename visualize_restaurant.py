import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set global plot style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

#load the data
menu_items = pd.read_csv('menu_items.csv')
order_details = pd.read_csv('order_details.csv')

#Merge the tables
merged_data = order_details.merge(menu_items, left_on='item_id', right_on='menu_item_id', how='left')

# Convert order_date to datetime
merged_data['order_date'] = pd.to_datetime(merged_data['order_date'])

print("Data loaded successfully!")
print(f"Total orders: {order_details['order_id'].nunique()}")
print(f"Total items ordered: {len(order_details)}")
print(f"Date range: {merged_data['order_date'].min()} to {merged_data['order_date'].max()}")

#1: Most and Least Ordered Items
plt.figure(figsize=(14, 6))
item_counts = merged_data.groupby('item_name').size().sort_values(ascending=False)

# Top 10 and Bottom 10
plt.subplot(1, 2, 1)
item_counts.head(10).plot(kind='barh', color='green')
plt.title('Top 10 Most Ordered Items', fontsize=14, fontweight='bold')
plt.xlabel('Number of Orders')
plt.gca().invert_yaxis()

plt.subplot(1, 2, 2)
item_counts.tail(10).plot(kind='barh', color='red')
plt.title('Top 10 Least Ordered Items', fontsize=14, fontweight='bold')
plt.xlabel('Number of Orders')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.savefig('most_least_ordered_items.png', dpi=300, bbox_inches='tight')
plt.show()

#2: Orders by Category
plt.figure(figsize=(10, 6))
category_counts = merged_data['category'].value_counts()
colors = sns.color_palette('husl', len(category_counts))

plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', 
        colors=colors, startangle=90)
plt.title('Distribution of Orders by Category', fontsize=16, fontweight='bold')
plt.savefig('orders_by_category.png', dpi=300, bbox_inches='tight')
plt.show()

#3: Top 5 Highest Spending Orders
order_totals = merged_data.groupby('order_id')['price'].sum().sort_values(ascending=False)
top_5_orders = order_totals.head(5)

plt.figure(figsize=(10, 6))
top_5_orders.plot(kind='bar', color='darkblue')
plt.title('Top 5 Highest Spending Orders', fontsize=16, fontweight='bold')
plt.xlabel('Order ID')
plt.ylabel('Total Spent ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.savefig('top_5_spending_orders.png', dpi=300, bbox_inches='tight')
plt.show()

#4: Category Breakdown of Highest Spending Order
highest_order_id = order_totals.idxmax()
highest_order_data = merged_data[merged_data['order_id'] == highest_order_id]
category_breakdown = highest_order_data.groupby('category').size()

plt.figure(figsize=(10, 6))
category_breakdown.plot(kind='bar', color='purple')
plt.title(f'Category Breakdown of Highest Spending Order (Order #{highest_order_id})', 
          fontsize=14, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Number of Items')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.savefig('highest_order_breakdown.png', dpi=300, bbox_inches='tight')
plt.show()

#5: Top 5 Orders - Category Composition
top_5_order_ids = order_totals.head(5).index
top_5_data = merged_data[merged_data['order_id'].isin(top_5_order_ids)]
category_composition = top_5_data.groupby(['order_id', 'category']).size().unstack(fill_value=0)

plt.figure(figsize=(12, 6))
category_composition.plot(kind='bar', stacked=True, colormap='Set3')
plt.title('Category Composition of Top 5 Highest Spending Orders', fontsize=14, fontweight='bold')
plt.xlabel('Order ID')
plt.ylabel('Number of Items')
plt.legend(title='Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('top_5_orders_composition.png', dpi=300, bbox_inches='tight')
plt.show()

#6: Orders Over Time
plt.figure(figsize=(14, 6))
daily_orders = merged_data.groupby(merged_data['order_date'].dt.date)['order_id'].nunique()
daily_orders.plot(kind='line', marker='o', color='teal', linewidth=2)
plt.title('Number of Orders Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Date')
plt.ylabel('Number of Orders')
plt.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('orders_over_time.png', dpi=300, bbox_inches='tight')
plt.show()

#7: Average Price by Category
plt.figure(figsize=(10, 6))
avg_price_by_category = menu_items.groupby('category')['price'].mean().sort_values(ascending=False)
avg_price_by_category.plot(kind='bar', color='orange')
plt.title('Average Dish Price by Category', fontsize=16, fontweight='bold')
plt.xlabel('Category')
plt.ylabel('Average Price ($)')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.savefig('avg_price_by_category.png', dpi=300, bbox_inches='tight')
plt.show()

#8: Order Size Distribution
plt.figure(figsize=(10, 6))
order_sizes = order_details.groupby('order_id').size()
plt.hist(order_sizes, bins=30, color='coral', edgecolor='black', alpha=0.7)
plt.title('Distribution of Order Sizes', fontsize=16, fontweight='bold')
plt.xlabel('Number of Items per Order')
plt.ylabel('Frequency')
plt.axvline(order_sizes.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {order_sizes.mean():.1f}')
plt.legend()
plt.grid(alpha=0.3)
plt.savefig('order_size_distribution.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nAll visualizations created and saved!")
print("Generated files:")
print("  - most_least_ordered_items.png")
print("  - orders_by_category.png")
print("  - top_5_spending_orders.png")
print("  - highest_order_breakdown.png")
print("  - top_5_orders_composition.png")
print("  - orders_over_time.png")
print("  - avg_price_by_category.png")
print("  - order_size_distribution.png")