##########################################################################
#
#    Tufts University, Comp 160 randSelect coding assignment  
#    main.py
#    randomized selection
#
#    simple main to test randSelect
#    NOTE: this main is only for you to test randSelect. We will compile
#          your code against a different main in our autograder directory
#
##########################################################################

from randSelect import randSelect
from randSelect import partition


def main():
	v = [53, 274, 89, 787, 417, 272, 110, 858, 922, 895, 39, 388, 549, 575, 340, 348, 872, 53, 163, 138, 345, 574, 341, 718, 251, 167, 1, 927, 446, 792, 89, 899, 611, 386, 71, 6, 323, 749, 459, 104, 927, 44, 94, 683, 145, 129, 809, 928, 21, 298, 933, 440, 587, 488, 271, 480, 857, 37, 787, 312, 351, 534, 820, 494, 211, 840, 623, 654, 539, 578, 828, 983, 322, 12, 407, 914, 787, 661, 525, 444, 701, 551, 653, 815, 682, 610, 911, 853, 497, 533, 684, 429, 383, 522, 32, 867, 772, 660, 185, 743, 839, 84, 935, 498, 673, 268, 174, 342, 345, 567, 400, 905, 75, 740, 467, 396, 586, 797, 344, 16, 193, 600, 90, 851, 643, 372, 13, 917, 360, 234, 415, 544, 513, 741, 843, 930, 61, 654, 294, 506, 987, 782, 645, 737, 238, 557, 495, 181, 157, 549, 455, 387, 769, 472, 45, 10, 137, 467, 197, 21, 262, 818, 360, 701, 278, 977, 444, 649, 430, 0, 111, 632, 64, 522, 363, 724, 90, 84, 443, 919, 8, 814, 548, 386, 75, 559, 710, 650, 413, 29, 330, 268, 978, 483, 33, 768, 575, 342, 424, 356, 24, 654, 651, 992, 167, 905, 986, 429, 65, 734, 890, 695, 147, 381, 684, 240, 761, 80, 844, 900, 642, 58, 776, 531, 396, 550, 313, 149, 935, 671, 790, 937, 298, 794, 855, 398, 377, 129, 547, 998, 345, 529, 122, 644, 170, 821, 603, 395, 442, 63, 759, 139, 465, 684, 21, 357, 460, 891, 756, 757, 737, 728, 684, 461, 311, 439, 810, 792, 28, 162, 534, 332, 892, 529, 527, 569, 140, 351, 512, 107, 558, 743, 377, 230, 914, 583, 348, 95, 278, 952, 518, 249, 208, 907, 329, 270, 407, 44, 960, 512, 82, 979, 201, 517, 204, 776, 912, 912, 17, 198, 274, 578, 236, 87, 614, 324, 85, 349, 567, 550, 136, 951, 911, 828, 957, 547, 138, 804, 923, 495, 504, 748, 407, 795, 28, 263, 730, 852, 848, 591, 887, 497, 348, 405, 936, 229, 860, 513, 947, 129, 624, 650, 6, 919, 812, 809, 615, 623, 993, 506, 351, 712, 598, 125, 707, 53, 369, 882, 471, 370, 980, 685, 876, 430, 323, 367, 221, 788, 459, 351, 830, 771, 197, 840, 185, 391, 1000, 825, 63, 861, 424, 384, 512, 271, 849, 946, 179, 876, 572, 385, 377, 70, 943, 303, 125, 930, 271, 514, 839, 619, 329, 56, 966, 389, 52, 600, 397, 305, 110, 476, 587, 783, 986, 723, 332, 248, 662, 456, 272, 861, 449, 576, 585, 352, 254, 971, 707, 466, 513, 588, 927, 945, 281, 345, 977, 49, 186, 126, 20, 438, 676, 508, 751, 135, 488, 547, 43, 481, 554, 144, 333, 891, 378, 912, 964, 226, 612, 884, 32, 474, 516, 921, 931, 908, 615, 792, 968, 295, 722, 594, 922, 14, 328, 747, 395, 233, 704, 909, 64, 892, 259, 291, 172, 426, 366, 435, 44, 621, 13, 508, 689, 168, 202, 47, 275, 537, 169, 782, 754, 949, 543, 859, 198, 310, 511, 886, 897, 478, 229, 289, 540, 94, 105, 453, 627, 558, 570, 286, 826, 199, 533, 963, 944, 69, 650, 961, 401, 416, 816, 810, 459, 113, 61, 583, 443, 779, 669, 446, 529, 365, 157, 505, 137, 199, 951, 216, 1000, 247, 995, 38, 250, 931, 213, 75, 413, 949, 26, 11, 422, 671, 329, 560, 30, 42, 946, 964, 252, 748, 908, 900, 873, 446, 715, 298, 949, 190, 311, 115, 289, 687, 658, 841, 332, 217, 527, 26, 766, 370, 804, 156, 477, 230, 424, 227, 522, 678, 942, 445, 400, 573, 193, 399, 78, 925, 508, 889, 43, 293, 142, 487, 748, 737, 934, 109, 129, 124, 471, 948, 882, 361, 565, 629, 17, 455, 533, 361, 295, 371, 218, 399, 959, 48, 108, 520, 849, 906, 771, 97, 607, 680, 332, 753, 84, 799, 684, 210, 982, 393, 184, 428, 129, 897, 486, 143, 871, 883, 5, 166, 807, 813, 88, 338, 33, 100, 149, 224, 468, 440, 959, 205, 677, 414, 61, 57, 155, 117, 472, 712, 92, 137, 684, 42, 367, 450, 979, 831, 839, 211, 836, 244, 240, 803, 441, 349, 687, 146, 91, 691, 9, 298, 335, 685, 410, 353, 805, 234, 834, 62, 59, 563, 66, 112, 946, 255, 294, 240, 128, 570, 811, 0, 803, 906, 619, 916, 785, 656, 880, 898, 873, 556, 269, 938, 430, 999, 568, 376, 379, 641, 133, 866, 426, 897, 34, 617, 296, 358, 320, 706, 861, 3, 819, 358, 518, 777, 2, 662, 301, 81, 387, 736, 188, 624, 333, 455, 880, 107, 751, 610, 979, 763, 546, 203, 408, 650, 694, 72, 196, 210, 739, 366, 437, 796, 492, 290, 669, 911, 566, 557, 167, 396, 27, 266, 746, 31, 782, 935, 922, 640, 688, 165, 798, 197, 374, 188, 103, 139, 731, 619, 103, 276, 124, 914, 936, 75, 369, 58, 936, 260, 369, 133, 258, 420, 94, 635, 266, 531, 811, 567, 884, 122, 682, 547, 123, 998, 938, 337, 293, 818, 820, 653, 887, 780, 673, 315, 450, 979, 240, 5, 95, 858, 115, 634, 103, 954, 785, 451, 857, 397, 837, 950, 906, 916, 367, 965, 690, 184, 839, 926, 135, 396, 0, 425, 214, 245, 937, 4, 827, 427, 132, 822, 867, 85, 178, 548, 273, 431, 172, 796, 905, 399, 847, 312, 66, 894, 24, 124, 810, 582, 403, 272, 582, 54, 653, 690, 556, 731, 192, 896, 317, 318, 611, 560, 803, 677, 346, 23, 681, 148, 315, 291, 901, 984, 204, 437, 217, 509, 46, 432, 67, 886, 818, 819, 994, 157, 174, 682, 48, 563, 227, 919, 849, 64, 459, 592, 988, 194, 410, 583, 735, 836, 882, 444, 728, 547, 961, 373, 76, 967, 850, 883, 221, 91, 449, 43, 961, 547, 948, 318, 718, 31, 213, 691, 36, 159, 875, 659, 537, 100, 731, 51, 857, 421, 816, 748, 904, 483, 630, 393, 341, 677]
	rankWeWant = 4
	ourNumber = randSelect(v, rankWeWant)
	expectedNumber = sorted(v)[rankWeWant]
	print("Expected ", expectedNumber, " our number ", ourNumber)
	if ourNumber != expectedNumber:
		print("Noooo!")
	else:
		print("Yayy!")


if __name__ == '__main__':
	main()