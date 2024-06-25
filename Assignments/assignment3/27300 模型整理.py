from collections import defaultdict


def sort_models(n, models):
    model_dict = defaultdict(list)

    # 将模型名称和参数量分离，并存储到字典中
    for model in models:
        name, size = model.split('-')
        model_dict[name].append(size)

    result = []
    # 对字典中的模型名称进行排序
    for name in sorted(model_dict.keys()):
        # 对每个模型的参数量进行排序
        sizes = sorted(model_dict[name], key=lambda x: float(x[:-1]) if x[-1] == 'M' else float(x[:-1]) * 1000)
        result.append(f"{name}: {', '.join(sizes)}")

    return result


# 读取输入
n = int(input())
models = [input().strip() for _ in range(n)]

# 调用函数进行排序
sorted_models = sort_models(n, models)

# 输出结果
for model in sorted_models:
    print(model)
