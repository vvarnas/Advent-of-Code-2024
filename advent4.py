# Specify the file path
file_path = "/Users/varnas/Desktop/vscode/input4"

# Read the file
with open(file_path, 'r') as file:
    lines = file.readlines()
# Remove any trailing newline characters from each line
lines = [line.strip() for line in lines]
# Print each line to confirm reading
#print("Processing data from file:", lines[-1][0])


sample_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

sample_data = sample_data.split('\n')

#Part 1
def count_XMAS(data):
    height = len(data)
    width = len(data[0])
    
    #Horizontal search
    #Scroll down, move left
    hori_count = 0
    for i in range(0, height):
        for j in range(0, width-3):
            char1 = data[i][j]
            char2 = data[i][j+1]
            char3 = data[i][j+2]
            char4 = data[i][j+3]
            word = char1 + char2 + char3 + char4
            if word == 'XMAS' or word == 'SAMX':
                hori_count +=1


    
    #Vertical search
    #Move left, scroll down
    verti_count = 0
    for i in range(0, width):
        for j in range(0, height-3):
            char1 = data[j][i]
            char2 = data[j+1][i]
            char3 = data[j+2][i]
            char4 = data[j+3][i]
            word = char1 + char2 + char3 + char4
            if word == 'XMAS' or word == 'SAMX':
                verti_count +=1

    
    #Diagonal search
    #Top left, bottom right
    diag1_count = 0
    for i in range(0, width-3):
        for j in range(0, height-3):
            char1 = data[i][j]
            char2 = data[i+1][j+1]
            char3 = data[i+2][j+2]
            char4 = data[i+3][j+3]
            word = char1 + char2 + char3 + char4
            if word == 'XMAS' or word == 'SAMX':
                diag1_count +=1

    
    #Diagonal search
    #Top right, bottom left
    diag2_count = 0
    for i in range(0, width-3):
        for j in range(3, height):
            char1 = data[i][j]
            char2 = data[i+1][j-1]
            char3 = data[i+2][j-2]
            char4 = data[i+3][j-3]
            word = char1 + char2 + char3 + char4
            if word == 'XMAS' or word == 'SAMX':
                diag2_count +=1

    return hori_count + verti_count + diag1_count + diag2_count
print(f"Total XMAS count: {count_XMAS(lines)}")


#Part 2
def count_XMAS_coords(data):
    height = len(data)
    width = len(data[0])
    
    #Diagonal search
    #Top left, Bottom right
    diag1_count = []
    for i in range(0, width-2):
        for j in range(0, height-2):
            char1 = data[i][j]
            char2 = data[i+1][j+1]
            char3 = data[i+2][j+2]
            word = char1 + char2 + char3 
            if word == 'MAS' or word == 'SAM':
                diag1_coord = ((i+1), (j+1))
                if len(diag1_coord) > 1:
                    diag1_count.append(diag1_coord)

    
    #Diagonal search
    #Bottom left, Top right
    diag2_count = []
    for i in range(0, width-2):
        for j in range(2, height):
            char1 = data[i][j]
            char2 = data[i+1][j-1]
            char3 = data[i+2][j-2]
            word = char1 + char2 + char3
            if word == 'MAS' or word == 'SAM':
                diag2_coord = ((i+1), (j-1))
                if len(diag2_coord) > 1:
                    diag2_count.append(diag2_coord)
    
    common_coords = list(set(map(tuple, diag1_count)) & set(map(tuple, diag2_count)))

    
    return len(common_coords)

print(f"Common diagonal MAS centre coordinates: {count_XMAS_coords(lines)}")