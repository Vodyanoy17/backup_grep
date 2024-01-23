events = {
    "updating_checkpoint_targeting": [
        20,
        [
            [1620, "config-configRS-65449d79a064331ae268a0ea"],
            [1623, "myShard_0"],
            [1626, "myShard_1"],
            [24181, "myShard_1"],
            [26401, "myShard_1"],
            [28344, "myShard_1"],
            [31762, "myShard_1"],
            [31989, "myShard_1"],
            [33169, "myShard_1"],
            [36418, "myShard_1"],
            [38931, "myShard_1"],
            [39169, "myShard_1"],
            [39541, "myShard_1"],
            [43658, "config-configRS-65449d79a064331ae268a0ea"],
            [44978, "myShard_1"],
            [45362, "myShard_1"],
            [45528, "config-configRS-65449d79a064331ae268a0ea"],
            [46004, "config-configRS-65449d79a064331ae268a0ea"],
            [46007, "myShard_0"],
            [46010, "myShard_1"],
        ],
    ],
    "successfully_released_lock": [
        23,
        [
            [2182, "config-configRS-65449d79a064331ae268a0ea"],
            [4168, "config-configRS-65449d79a064331ae268a0ea"],
            [5804, "config-configRS-65449d79a064331ae268a0ea"],
            [7349, "config-configRS-65449d79a064331ae268a0ea"],
            [8884, "config-configRS-65449d79a064331ae268a0ea"],
            [9981, "config-configRS-65449d79a064331ae268a0ea"],
            [12266, "config-configRS-65449d79a064331ae268a0ea"],
            [13830, "config-configRS-65449d79a064331ae268a0ea"],
            [15487, "config-configRS-65449d79a064331ae268a0ea"],
            [17038, "config-configRS-65449d79a064331ae268a0ea"],
            [19581, "config-configRS-65449d79a064331ae268a0ea"],
            [21132, "config-configRS-65449d79a064331ae268a0ea"],
            [22985, "myShard_0"],
            [25228, "myShard_0"],
            [27059, "myShard_0"],
            [28310, "myShard_1"],
            [31382, "myShard_0"],
            [32510, "myShard_0"],
            [35403, "config-configRS-65449d79a064331ae268a0ea"],
            [36920, "myShard_1"],
            [48547, "myShard_1"],
            [48779, "config-configRS-65449d79a064331ae268a0ea"],
            [49377, "myShard_0"],
        ],
    ],
}
events = {'updating_checkpoint_targeting': [7,
                                   [[397155, 'sh2_pet'],
                                    [397976, 'sh2_pet'],
                                    [609278, 'sh2_pet'],
                                    [610302, 'sh2_pet'],
                                    [874794,
                                     'config-config_dsit-63881227a4c004603837fadf'],
                                    [874852, 'sh2_dsit'],
                                    [874873, 'sh1_dsit']]],
 'successfully_released_lock': [32,
                                [[33026, 'rs_sadi_dev'],
                                 [634499,
                                  'config-config_pet-63894b0509d7a34ef767ce1c'],
                                 [636429, 'sh2_pet'],
                                 [636613, 'sh1_pet'],
                                 [636856, 'sh3_pet'],
                                 [703760, 'rs_sadi_dsit'],
                                 [779150, 'sh1_dev'],
                                 [779359,
                                  'config-config_dev-636ddc9a8be2fc75acfccf5b'],
                                 [780001, 'sh3_dev'],
                                 [780053, 'sh2_dev'],
                                 [798540,
                                  'config-config_dsit-63883b4ea4c00460383d5f3b'],
                                 [799490, 'sh1_pet'],
                                 [800528, 'sh1_dsit'],
                                 [800553, 'sh2_pet'],
                                 [800930, 'sh3_dsit'],
                                 [800959, 'sh2_dsit'],
                                 [801518,
                                  'config-config_pet-637559c68be2fc75ac3966bc'],
                                 [804511, 'shard4_pet'],
                                 [805716, 'shard3_pet'],
                                 [810379,
                                  'config-config_pet-65295f1ac7a7dd5714ded457'],
                                 [810856, 'shard5_pet'],
                                 [812742, 'shard1_eite'],
                                 [813113,
                                  'config-config_eite-6504ad2511f0456cf9e4d4f3'],
                                 [815268, 'shard6_pet'],
                                 [816245, 'shard1_pet'],
                                 [817900, 'shard8_pet'],
                                 [821198, 'shard7_pet'],
                                 [821614, 'shard2_pet'],
                                 [852262, 'rs_sadi_eite'],
                                 [860075,
                                  'config-configRS-64653c11b675bd4b4f47d113'],
                                 [862012, 'myShard_1'],
                                 [866270, 'myShard_0']]]}


def find_event_pairs(events):
    # Copy the starting and finishing events
    starting_events = events["updating_checkpoint_targeting"][1].copy()
    finishing_events = events["successfully_released_lock"][1]

    # Sort events by line number
    starting_events.sort(key=lambda x: x[0])
    finishing_events.sort(key=lambda x: x[0])

    # Lists to store pairs, unmatched finishing events, and additional unmatched starting events
    event_pairs = []
    unmatched_finishing_events = []

    for finishing_event in finishing_events:
        min_distance = float('inf')
        # Find the closest starting event with the same replicaset and smaller line number
        candidate_starting_event = None
        for starting_event in reversed(starting_events):
            if starting_event[1] == finishing_event[1] and starting_event[0] < finishing_event[0]:
                distance = finishing_event[0] - starting_event[0]
                if distance < min_distance:
                    min_distance = distance
                    candidate_starting_event = starting_event

        if candidate_starting_event:
            # Add the pair to the list
            event_pairs.append((candidate_starting_event, finishing_event))
            starting_events.remove(candidate_starting_event)  # Remove the used starting event
        else:
            # Add unmatched finishing event to the list
            unmatched_finishing_events.append(finishing_event)

    # Return the results
    return event_pairs, unmatched_finishing_events, starting_events

# Call the function and get the results
event_pairs, unmatched_finishing, unmatched_starting = find_event_pairs(events)

# Print the results
print("Event Pairs:")
for pair in event_pairs:
    print(pair)

print("\nUnmatched Finishing Events:")
for event in unmatched_finishing:
    print(event)

print("\nAdditional Unmatched Starting Events:")
for event in unmatched_starting:
    print(event)