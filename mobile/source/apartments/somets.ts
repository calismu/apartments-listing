type TCars = string[];

interface IPerson {
	name: string,
	age: number,
	cars?: TCars,
};

let p: IPerson = {
	name: "Ahmed",
	age: 39,
	cars: ['BMW',],
};

function displayPerson(p: IPerson): string {
	return JSON.stringify(p);
}

const res: string = displayPerson(p);
console.log(res);