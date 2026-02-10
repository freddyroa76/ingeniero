// Test formatNPS function
function formatNPS(nps) {
  const npsFloat = parseFloat(nps);
  
  // Map of decimal values to fractional representations
  const fractionMap = {
    0.125: '1/8"',
    0.25: '1/4"',
    0.375: '3/8"',
    0.5: '1/2"',
    0.75: '3/4"',
    1.25: '1-1/4"',
    1.5: '1-1/2"',
    2.5: '2-1/2"',
    3.5: '3-1/2"'
  };
  
  // Check if this NPS has a fractional representation
  if (fractionMap[npsFloat]) {
    return fractionMap[npsFloat];
  }
  
  // For whole numbers, add inch symbol
  if (Number.isInteger(npsFloat)) {
    return npsFloat + '"';
  }
  
  // For other decimals, return as-is with inch symbol
  return npsFloat + '"';
}

// Test all NPS sizes
const testSizes = [0.125, 0.25, 0.375, 0.5, 0.75, 1, 1.25, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 30, 32, 34, 36, 42];

console.log("NPS Size Formatting Test:");
console.log("=".repeat(50));

testSizes.forEach(size => {
  const formatted = formatNPS(size);
  console.log(`${size.toString().padEnd(6)} => ${formatted}`);
});

console.log("\n" + "=".repeat(50));
console.log("Expected fractional formats:");
console.log("  0.125  => 1/8\"");
console.log("  0.25   => 1/4\"");
console.log("  0.375  => 3/8\"");
console.log("  0.5    => 1/2\"");
console.log("  0.75   => 3/4\"");
console.log("  1.25   => 1-1/4\"");
console.log("  1.5    => 1-1/2\"");
console.log("  2.5    => 2-1/2\"");
console.log("  3.5    => 3-1/2\"");
console.log("  Others => [number]\"");
