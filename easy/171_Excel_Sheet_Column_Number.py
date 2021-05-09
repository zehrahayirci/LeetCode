class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnTitle = columnTitle[::-1]
        add=0
        for i, item in enumerate(columnTitle):
            add+=(26**i)*(ord(item)-64)
        return add
        