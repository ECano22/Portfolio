#include <conio.h>
#include <array>
#include "Input.h"

std::array<int, 2> Movement()
{
	std::array<int, 2> returnValue;
	int key = _getch();
	if (key == 224 || key == 0) key = _getch();

	switch (key)
	{
		case 72:
		case 'w':
		case 'W':
			returnValue = { 0, -1 };
			break;
		case 75:
		case 'a':
		case 'A':
			returnValue = { 1, 0 };
			break;
		case 80:
		case 's':
		case 'S':
			returnValue = { 0, 1 };
			break;
		case 77:
		case 'd':
		case 'D':
			returnValue = { -1, 0 };
			break;
		default:
			returnValue = { 0,0 };
	}
	return returnValue;
}