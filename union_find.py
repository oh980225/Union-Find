# 부모 노드를 찾는 함수
def get_parent(parent_list, element):
  if parent_list[element] == element:
    return element
  parent_list[element] = get_parent(parent_list, parent_list[element])
  return parent_list[element]

# 두 부모 노드를 합치는 함수
def union_parent(parent_list, element1, element2):
  element1 = get_parent(parent_list, element1)
  element2 = get_parent(parent_list, element2)
  if element1 < element2:
    parent_list[element2] = element1
  else:
    parent_list[element1] = element2

# 같은 부모 노드를 가지는지 확인하는 함수
def find_parent(parent_list, element1, element2):
  element1 = get_parent(parent_list, element1)
  element2 = get_parent(parent_list, element2)
  if element1 == element2:
    return True
  return False