#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
利息计算器
输入本金、时间和利率，计算预期利息
"""

def calculate_interest(principal, time, rate):
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

def main():
    """主函数"""
    print("=== 利息计算器 ===")
    print("请输入以下信息：")
    
    try:
        # 获取用户输入
        principal = float(input("本金（元）: "))
        time = float(input("时间（年）: "))
        rate = float(input("年利率（%）: "))
        
        # 验证输入
        if principal <= 0 or time <= 0 or rate <= 0:
            print("错误：所有输入值必须大于0")
            return
        
        # 计算利息
        interest = calculate_interest(principal, time, rate)
        
        # 输出结果
        print("\n=== 计算结果 ===")
        print(f"本金: {principal:.2f} 元")
        print(f"时间: {time:.2f} 年")
        print(f"年利率: {rate:.2f}%")
        print(f"预期利息: {interest:.2f} 元")
        print(f"本息合计: {principal + interest:.2f} 元")
        
    except ValueError:
        print("错误：请输入有效的数字")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()