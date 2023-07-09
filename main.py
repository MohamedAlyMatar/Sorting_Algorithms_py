import pygame
import random
import math
# from algorithms import bubble_sort, insertion_sort
pygame.init()

# -------------------------------- algoritims definitions start --------------------------------

def bubble_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_list(draw_info, {j: draw_info.GREEN, j + 1: draw_info.RED}, True)
				yield True

	return lst


def insertion_sort(draw_info, ascending=True):
	lst = draw_info.lst

	for i in range(1, len(lst)):
		current = lst[i]

		while True:
			ascending_sort = i > 0 and lst[i - 1] > current and ascending
			descending_sort = i > 0 and lst[i - 1] < current and not ascending

			if not ascending_sort and not descending_sort:
				break

			lst[i] = lst[i - 1]
			i = i - 1
			lst[i] = current
			draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
			yield True

	return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        min_idx = i

        # Find the minimum element in the remaining unsorted part of the array
        for j in range(i+1, len(lst)):
            if (lst[j] < lst[min_idx] and ascending) or (lst[j] > lst[min_idx] and not ascending):
                min_idx = j

        # Swap the found minimum element with the first element
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
        yield True

    return lst


def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    if len(lst) <= 1:
        return lst
    
    stack = [(0, len(lst)-1)]  # Initialize stack with initial left and right indices
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            pivot_idx = partition(draw_info, lst, low, high)
            
            # Push indices of the two subarrays onto the stack
            stack.append((low, pivot_idx - 1))
            stack.append((pivot_idx + 1, high))
            
            yield True
    
    return lst


def partition(draw_info, arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)

    return i + 1


# -------------------------------- algoritims definitions end --------------------------------


class DrawInformation:
    # COLORS
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED   = 255, 0, 0
    BLUE  = 0, 0, 255
    BACKGROUND_COLOR = WHITE

    # BARS COLORS
    BARS = [
        (128, 128, 128),
        (160,160,160),
        (192,192,192)
    ]

    # FONTS
    FONT = pygame.font.SysFont("comicsans", 20)
    LARGE_FONT = pygame.font.SysFont("comicsans", 30)

    # PADDING
    SIDE_PAD = 100
    TOP_PAD  = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Python Sorting Algorithms Visualizer")
        self.set_list(lst)

    
    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_value - self.min_value))
        self.start_x = self.SIDE_PAD // 2


def draw(draw_info, algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.GREEN)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 5))
    
    controls = draw_info.FONT.render("R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 45))

    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort | Q - Quick Sort | S - Selection Sort ", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2 , 75))
    
    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info, color_pos={}, clear_bg=False):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
					  draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_value) * draw_info.block_height
        
        color_bar = draw_info.BARS[i % 3]
        if i in color_pos:
            color_bar = color_pos[i]

        pygame.draw.rect(draw_info.window, color_bar, (x, y, draw_info.block_width, draw_info.height))

    if clear_bg:
        pygame.display.update()


def generate_list(n, min, max):
    lst = []
    
    for _ in range(n):
        value = random.randint(min, max)
        lst.append(value)
    
    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)
    sorting = False
    ascending = True

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        clock.tick(5)
        # clock.tick(60)
        # clock.tick(120)
        
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                lst = generate_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "insertion sort"
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "bubble sort"
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "selection sort"
            elif event.key == pygame.K_q and not sorting:
                sorting_algorithm = quick_sort
                sorting_algo_name = "quick sort"
            

    pygame.quit()


if __name__ == "__main__":
    main()