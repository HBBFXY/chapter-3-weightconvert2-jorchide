# 初始地球体重（单位：kg），可自行调整
initial_earth_weight = 60
# 每年在地球上的体重增长量（单位：kg）
annual_growth = 0.5
# 月球体重与地球体重的比例（16.5%）
moon_ratio = 0.165

# 输出表头
print("未来10年地球与月球体重变化表")
print("-" * 40)
print(f"{'年份':<8}{'地球体重(kg)':<15}{'月球体重(kg)':<15}")
print("-" * 40)

# 循环计算并输出未来10年的体重
for year in range(1, 11):
    current_earth_weight = initial_earth_weight + annual_growth * year
    current_moon_weight = current_earth_weight * moon_ratio
    # 保留2位小数，使输出更规整
    print(f"{year:<8}{current_earth_weight:<15.2f}{current_moon_weight:<15.2f}")

