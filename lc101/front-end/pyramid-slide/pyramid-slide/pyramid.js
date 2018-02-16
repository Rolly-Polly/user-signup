function drawPyramid() {
    
         document.getElementById("pyramid").innerHTML = '';
         var symbol = document.getElementById("brickStyle").value;
         var height = document.getElementById("howHigh").value;
         console.log(symbol)

         for (var row = 0; row < height; row++) {
    
            
             var numBricks = row + 2;
             var numSpaces = height - row - 1;
         
             var rowStr = "";
             for (var i = 0; i < numSpaces; i++) {
                 var spaceChar = "&nbsp";
                 rowStr += spaceChar;
             }
             for (var i = 0; i < numBricks; i++) {
                 rowStr += symbol;
             }
        
            
            rowElem = document.createTextNode(rowStr);
    
            
            rowElem = document.createElement("p");
            rowElem.innerHTML = rowStr;
    
            
            document.getElementById("pyramid").appendChild(rowElem);
            document.getElementById("pyramidHeight").innerHTML = height;
    
        }
    };
    drawPyramid()