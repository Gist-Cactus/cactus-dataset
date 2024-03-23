import random
import cv2

path = 'C:/Users/User/AI4GOOD_Cactus/dataset/slide_dataset/'

# 주어진 여러 집합
position = ['2분할', '3분할', '6분할', '36분할', '216분할', '1296분할']
axis = ['가로', '세로']
scale = ['영역_2분할', '영역_3분할', '영역_6분할', '영역_36분할', '영역_216분할', '영역_1296분할']
relation = ['Orientation', 'Behavioral_description', 'Annotation', 'Association']
category = ['Title', 'Text', 'Diagram', 'Natural_Image', 'PPT_Object', 'Table']
contents = ['Title_contents', 'Text_contents']
sets = [position, axis, scale, relation, category, contents]

# 각 집합에서 하나 이상의 요소를 무작위로 선택하여 내보내는 함수
def select_elements_from_sets(sets):
    selected_elements = []
    for s in sets:
        selected_elements.append(random.choice(list(s)))
    return selected_elements

def select_example_from_dataset():
    example_num = random.randrange(1, 10001)
    return example_num


questions = select_elements_from_sets(sets)
print("Selected elements:", questions)

slide_num = select_example_from_dataset()
example = cv2.imread(path + 'slide_' + str(slide_num) + '.jpg')
cv2.imshow('Test Image ' + str(slide_num), example)
cv2.waitKey()