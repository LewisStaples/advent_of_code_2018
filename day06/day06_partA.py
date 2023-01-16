#!/usr/bin/env python3

# adventOfCode 20xy day 6
# https://adventofcode.com/20xy/day/6


# key is the point itself
# value is another dict with:
#   which group of points this point is in (index in input file)
#   manhattan distance from the original point for that group
point_collection = dict()


def get_input(input_filename):
    # Reading input from the input file
    print(f"\nUsing input file: {input_filename}\n")
    with open(input_filename) as f:
        # Pull in each line from the input file
        for group_number, in_string in enumerate(f):
            in_string = in_string.rstrip()
            x, y = in_string.split(", ")
            x, y = (int(z) for z in (x, y))
            point_collection[(x, y)] = {"group_number": group_number, "manh_dist": 0}
    return point_collection


def get_outer_box(point_collection):
    ret_val = {
        "x_min": float("inf"),
        "x_max": float("-inf"),
        "y_min": float("inf"),
        "y_max": float("-inf"),
    }
    for x, y in point_collection:
        ret_val["x_min"] = min(ret_val["x_min"], x)
        ret_val["x_max"] = max(ret_val["x_max"], x)
        ret_val["y_min"] = min(ret_val["y_min"], y)
        ret_val["y_max"] = max(ret_val["y_max"], y)
    return ret_val


def special_print(set_pts, point_collection, manh_dist):
    """
    Used for debugging, if needed
    """
    the_groups = list({x["group_number"] for x in point_collection.values()})
    while None in the_groups:
        the_groups.remove(None)

    for group in the_groups:
        print(f"Grp {group}: ", end="")
        for k, v in point_collection.items():
            if v["group_number"] == group:
                if v["manh_dist"] == manh_dist:
                    print(k, end=", ")
        print()
    print(set_pts)


def extend_til_shown_infinite(point_collection, outer_box):
    manh_dist = 0
    while True:
        set_pts = {
            k
            for k, v in point_collection.items()
            if v["manh_dist"] == manh_dist and v["group_number"] is not None
        }

        # if all set_pts outside outer_box, return set_pts
        flag = True
        for pt in set_pts:
            if pt[0] <= outer_box["x_max"]:
                if pt[0] >= outer_box["x_min"]:
                    if pt[1] <= outer_box["y_max"]:
                        if pt[1] >= outer_box["y_min"]:
                            flag = False
        if flag:
            return set_pts

        manh_dist += 1
        for pt in set_pts:
            # find points one step away
            for direction in [[0, -1], [0, 1], [1, 0], [-1, 0]]:
                new_pt = (pt[0] + direction[0], pt[1] + direction[1])
                if new_pt in point_collection:
                    if (
                        point_collection[new_pt]["group_number"]
                        == point_collection[pt]["group_number"]
                    ):
                        continue
                    if point_collection[new_pt]["manh_dist"] == manh_dist:
                        point_collection[new_pt]["group_number"] = None
                    else:
                        assert point_collection[new_pt]["manh_dist"] < manh_dist
                else:
                    point_collection[new_pt] = {
                        "group_number": point_collection[pt]["group_number"],
                        "manh_dist": manh_dist,
                    }


def get_infinite_groups(point_collection, last_pts):
    infinite_groups = set()
    for l_pt in last_pts:
        infinite_groups.add(point_collection[l_pt]["group_number"])
    return infinite_groups


def get_size_largest_noninfinite_group(point_collection, infinite_groups):
    group_sizes = dict()
    for point in point_collection:
        group_number = point_collection[point]["group_number"]
        if group_number in infinite_groups:
            continue
        if group_number is None:
            continue
        if group_number not in group_sizes:
            group_sizes[group_number] = 1
        else:
            group_sizes[group_number] += 1

    return max(group_sizes.values())


def solve_problem(input_filename):
    point_collection = get_input(input_filename)
    outer_box = get_outer_box(point_collection)
    last_pts = extend_til_shown_infinite(point_collection, outer_box)
    infinite_groups = get_infinite_groups(point_collection, last_pts)
    size_largest_noninfinite_group = get_size_largest_noninfinite_group(
        point_collection, infinite_groups
    )

    print(
        f"The size of the largest non-infinite group is: \
            {size_largest_noninfinite_group}\n"
    )


solve_problem("input_sample0.txt")
