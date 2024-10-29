def merge_k_lists(lists):
    
    def merge_two_lists(list1, list2):
        merged = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        while i < len(list1):
            merged.append(list1[i])
            i += 1
    
        while j < len(list2):
            merged.append(list2[j])
            j += 1
        
        return merged

    if not lists:
        return []
    

    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):

                merged_lists.append(merge_two_lists(lists[i], lists[i + 1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists
    
    return lists[0]

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)