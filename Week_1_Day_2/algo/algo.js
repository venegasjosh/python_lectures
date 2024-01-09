/* 

Acronyms

Crate a function that, given a string, returns the string's acronym (first letter of each word capitalized).

Do it with .split() first if you need to, then try to do it without

*/

const str1 = 'object oriented programming';

const expected1 = 'OOP';

// The 4 pillars of OOP

const str2 = 'abstraction polymorphism inheritance encapsulation';
const expected2 = "APIE";

const str3 = 'software development life cycle';

const expected3 = 'SDLC';

//BONUS: ignore extra spaces

const str4 = 'global information tracker';
const expected4 = "GIT";

// Turns the given str into an acronym.Turns
// Time : 0(?)
// Space: 0(?)

// @param {String} str A string to be turned into an acroynm
// @returns {String} The Acroynm

function acronymize(str) {
  // Step 1: trim the input string to remove any extra spaces at the start and the end - .trim()

  // Step 2: Initialize a variable to hold the acronym, initially empty

  // Step 3: Split the input into an array of words - .split()

  // Step 4: Loop through each word in the array
  //   Step 4.1: Check if the current word is not an empty string
  //   Step 4.2: Take the first character of the word, convert it to uppercase, and add it to the acroynm

  //Step 5: Return the constructed acroynm
}

const result1 = acronymize(str1);
console.log(result1);

const result2 = acronymize(str2);
console.log(result2);

const result3 = acronymize(str3);
console.log(result3)

const result4 = acronymize(str4);
console.log(result4)











// function acronymizeWithSplit(wordsStr = "") {
//   let acronym = "";
//   const wordsArr = wordsStr.split(" ");

//   for (const word of wordsArr) {
//     // Splitting can result in empty strings.
//     if (word !== "") {
//       // upper case each letter as it's added so toUpperCase doesn't have
//       // to loop over each acronym char at the end to upper case.
//       acronym += word[0].toUpperCase();
//     }
//   }
//   return acronym;
// }







// function acronymize(wordsStr = "") {
//   let acronym = "";

//   for (let i = 0; i < wordsStr.length; i++) {
//     // These booleans add readability because they are named descriptively,
//     // they also simplify how many conditional statements or nested conditions
//     // are needed.
//     const currentChar = wordsStr[i];
//     const isCurrentCharSpace = currentChar === " ";
//     const isPreviousCharSpace = wordsStr[i - 1] === " ";
//     const isFirstLetterOfWord =
//       (i === 0 && !isCurrentCharSpace) ||
//       (!isCurrentCharSpace && isPreviousCharSpace);

//     if (isFirstLetterOfWord) {
//       acronym += currentChar.toUpperCase();
//     }
//   }
//   return acronym;
// }