class Solution:
    def smallestNumber(self, num: int) -> int:
        sign = ""

        if num < 0:
            sign = "-"
            num = num * (-1)

        arr = [int(value) for value in str(num)]

        result = 0
        if sign:

            arr.sort(reverse = True)

            result = int("".join(str(x) for x in arr))

            return -1 * result

        else:
            arr.sort()

            if arr[0] == 0:
                left = 0
                right = 0

                while right < len(arr):

                    if arr[right] != 0:
                        arr[left], arr[right] = arr[right], arr[left]
                        break

                    right += 1

                result = int("".join(str(x) for x in arr))

                return result

            else:

                result = int("".join(str(x) for x in arr))

                return result