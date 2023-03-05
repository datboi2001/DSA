def rewire_elevator(floors: list[int]) -> list[int]:
    pass # your code here!

if __name__ == "__main__":
    # sample cases -- you can modify, remove, or leave these statements in

    print("Testing sample case 1...", end="")
    case1_input = [-1, 1, 2, 3, 4, 5]
    case1_output = rewire_elevator(case1_input)
    try:
        assert case1_output is not None
        assert case1_output[2] == -1, "The third element must take you to floor -1"
        assert sum(case1_output) == sum(case1_input), "The sum of the floors must not change"
        assert len(set(case1_output)) == len(case1_output), "There must not be any duplicate floors in your output"
    except Exception as e:
        print("\nYour output: " + repr(case1_output))
        raise e
    print("Passed!")

    print("Testing sample case 2...", end="")
    case2_input = [-1, 1, 2, 3]
    case2_output = rewire_elevator(case2_input)
    try:
        assert case2_output is not None
        assert case2_output[2] == -1, "The third element must take you to floor -1. Your third element: "
        assert sum(case2_output) == sum(case2_input), "The sum of the floors must not change"
        assert len(set(case2_output)) == len(case2_output), "There must not be any duplicate floors in your output"
    except Exception as e:
        print("\nYour output: " + repr(case2_output))
        raise e

    print("Passed!")