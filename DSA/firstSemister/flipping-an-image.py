class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in range(len(image)):
            for col in range(len(image)//2):
                image[row][col],image[row][len(image)-1-col] = image[row][len(image)-1-col],image[row][col]
                image[row][col] = 1 - image[row][col]
                image[row][len(image)-1-col] = 1 - image[row][len(image)-1-col]
            if len(image)%2:
                image[row][len(image)//2] = 1 - image[row][len(image)//2 ] 
        return image
