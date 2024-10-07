// Problem Name: 36. valid Sudoku
// Problem Link: https://leetcode.com/problems/valid-sudoku/description/

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set seenValuesAndContext=new HashSet();
        for(int rowNumber=0;rowNumber<9;rowNumber++){
            for(int colNumber=0;colNumber<9;colNumber++){
                char value=board[rowNumber][colNumber];
                if(value!='.'){
                    String currentlySeenValueRow="row"+rowNumber+"val"+value;
                    String currentlySeenValueCol="col"+colNumber+"val"+value;
                    String currentlySeenValueGrid="grid"+(Math.floorDiv(rowNumber,3)*3+Math.floorDiv(colNumber,3))+"val"+value;
                    if(seenValuesAndContext.contains(currentlySeenValueRow) || seenValuesAndContext.contains(currentlySeenValueCol) || seenValuesAndContext.contains(currentlySeenValueGrid)){
                        return false;
                    }
                    seenValuesAndContext.add(currentlySeenValueRow);
                    seenValuesAndContext.add(currentlySeenValueCol);
                    seenValuesAndContext.add(currentlySeenValueGrid);
                }
            }
        }
        return true;  
    }
}
