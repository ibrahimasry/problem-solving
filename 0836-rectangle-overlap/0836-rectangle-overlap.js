/**
 * @param {number[]} rec1
 * @param {number[]} rec2
 * @return {boolean}
 */
var isRectangleOverlap = function(rec1, rec2) {
        let x1 = rec1[0], y1 = rec1[1], x2 = rec1[2], y2 = rec1[3];
        let x3 = rec2[0], y3 = rec2[1], x4 = rec2[2], y4 = rec2[3];
        let overlapX = false;
        let overlapY = false;
        if(Math.max(x1, x3) < Math.min(x2, x4))
            overlapX = true;
        if(Math.max(y1, y3) < Math.min(y2, y4))
            overlapY = true;
        return overlapX && overlapY;

};