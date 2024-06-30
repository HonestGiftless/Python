# sort_priority() 🌶️

def sort_priority(values, group):
    result_groups = sorted(group)
    result_values = sorted([i for i in values if i not in result_groups])
    result_groups = sorted([j for j in group if j in values])

    values[:] = result_groups + result_values