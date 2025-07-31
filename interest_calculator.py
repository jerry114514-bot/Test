#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
利息计算器
输入本金、时间和利率，计算预期利息（支持简单利息和复利）
"""

def calculate_simple_interest(principal, time, rate):
    """
    计算简单利息
    
    参数:
    principal (float): 本金
    time (float): 时间（年）
    rate (float): 年利率（百分比，如 5.0 表示 5%）
    
    返回:
    float: 预期利息
    """
    # 将百分比转换为小数
    rate_decimal = rate / 100
    # 计算利息：本金 × 利率 × 时间
    interest = principal * rate_decimal * time
    return interest

def calculate_compound_interest(principal, time, rate, compound_frequency=1):
    """
    计算复利
    
    参数:
    principal (float): 本金
    time (float): 时间（年）
    rate (float): 年利率（百分比，如 5.0 表示 5%）
    compound_frequency (int): 复利频率（1=年复利，2=半年复利，4=季度复利，12=月复利，365=日复利）
    
    返回:
    tuple: (利息, 本息合计)
    """
    # 将百分比转换为小数
    rate_decimal = rate / 100
    # 复利公式：A = P(1 + r/n)^(nt)
    # 其中 A 是最终金额，P 是本金，r 是年利率，n 是复利频率，t 是时间
    final_amount = principal * (1 + rate_decimal / compound_frequency) ** (compound_frequency * time)
    interest = final_amount - principal
    return interest, final_amount

def main():
    """主函数"""
    print("=== 利息计算器 ===")
    print("支持简单利息和复利计算")
    print()
    
    try:
        # 获取用户输入
        principal = float(input("本金（元）: "))
        time = float(input("时间（年）: "))
        rate = float(input("年利率（%）: "))
        
        # 验证输入
        if principal <= 0 or time <= 0 or rate <= 0:
            print("错误：所有输入值必须大于0")
            return
        
        print("\n请选择计算方式：")
        print("1. 简单利息")
        print("2. 复利")
        choice = input("请输入选择 (1 或 2): ").strip()
        
        if choice == "1":
            # 计算简单利息
            interest = calculate_simple_interest(principal, time, rate)
            final_amount = principal + interest
            
            print("\n=== 简单利息计算结果 ===")
            print(f"本金: {principal:.2f} 元")
            print(f"时间: {time:.2f} 年")
            print(f"年利率: {rate:.2f}%")
            print(f"预期利息: {interest:.2f} 元")
            print(f"本息合计: {final_amount:.2f} 元")
            
        elif choice == "2":
            # 选择复利频率
            print("\n请选择复利频率：")
            print("1. 年复利")
            print("2. 半年复利")
            print("3. 季度复利")
            print("4. 月复利")
            print("5. 日复利")
            
            freq_choice = input("请输入选择 (1-5): ").strip()
            
            frequency_map = {
                "1": 1,    # 年复利
                "2": 2,    # 半年复利
                "3": 4,    # 季度复利
                "4": 12,   # 月复利
                "5": 365   # 日复利
            }
            
            if freq_choice in frequency_map:
                compound_frequency = frequency_map[freq_choice]
                interest, final_amount = calculate_compound_interest(principal, time, rate, compound_frequency)
                
                frequency_names = {
                    1: "年复利",
                    2: "半年复利", 
                    4: "季度复利",
                    12: "月复利",
                    365: "日复利"
                }
                
                print(f"\n=== 复利计算结果 ({frequency_names[compound_frequency]}) ===")
                print(f"本金: {principal:.2f} 元")
                print(f"时间: {time:.2f} 年")
                print(f"年利率: {rate:.2f}%")
                print(f"复利频率: {frequency_names[compound_frequency]}")
                print(f"预期利息: {interest:.2f} 元")
                print(f"本息合计: {final_amount:.2f} 元")
                
                # 对比简单利息
                simple_interest = calculate_simple_interest(principal, time, rate)
                difference = interest - simple_interest
                print(f"\n与简单利息的差异: {difference:.2f} 元")
                
            else:
                print("无效选择，使用年复利")
                interest, final_amount = calculate_compound_interest(principal, time, rate)
                print(f"\n=== 复利计算结果 (年复利) ===")
                print(f"本金: {principal:.2f} 元")
                print(f"时间: {time:.2f} 年")
                print(f"年利率: {rate:.2f}%")
                print(f"预期利息: {interest:.2f} 元")
                print(f"本息合计: {final_amount:.2f} 元")
        else:
            print("无效选择，程序退出")
            
    except ValueError:
        print("错误：请输入有效的数字")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()