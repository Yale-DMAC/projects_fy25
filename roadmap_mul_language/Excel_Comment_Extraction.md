Use Excel Scripts to run the following:
```
function main(workbook: ExcelScript.Workbook) {
    let sheet: ExcelScript.Worksheet = workbook.getActiveWorksheet();
    let comments: ExcelScript.Comment[] = sheet.getComments();

    // Define the output column (e.g., column E, which is index 4)
    const outputColumnIndex = 4;

    for (let comment of comments) {
        let range: ExcelScript.Range = comment.getLocation();
        let row: number = range.getRowIndex();
        let col: number = range.getColumnIndex();

        // Only process comments in column D (index 3)
        if (col === 3) {
            let commentText: string = comment.getContent();
            sheet.getCell(row, outputColumnIndex).setValue(commentText);
        }
    }
}
```