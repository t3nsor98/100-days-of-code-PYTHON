function findAnagrams(array) {
  return array.filter((ana) => {
    const str1 = ana[0].toLowerCase().trim();
    const str2 = ana[1].toLowerCase().trim();

    // edge case to see if both have same length or not
    if (str1.length !== str2.length) {
      return false;
    }

    // lets sort both strings and compare them Yo ho ho
    const sortedStr1 = str1.split("").sort().join("");
    const sortedStr2 = str2.split("").sort().join("");
    return sortedStr1 === sortedStr2;
  });
}

console.log(findAnagrams(anagrams));
