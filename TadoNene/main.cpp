#include <iostream>


class Date {
	int year_;
	int month_;
	int day_;

public:
	void SetDate(int year, int month, int date);
	void AddDay(int inc);
	void AddMonth(int inc);
	void AddYear(int inc);

	int GetCurrentMonthTotalDays(int year, int month);

	void ShowDate();
};

void Date::SetDate(int year, int month, int day) {
	year_ = year;
	month_ = month;
	day_ = day;
}

int Date::GetCurrentMonthTotalDays(int year, int month) {
	static int month_day[12] =
	{ 31, 28, 31, 30,
	  31, 31, 30, 31,
	  30, 31, 30, 31 };

	if (month != 2) { return month_day[month - 1]; } // n월
	else if (year % 4 == 0 && year % 100 != 0) { return 29; } // 윤년
	else { return 28;  }	// 2월
}

void Data::AddDay(int inc) {
	while (true)
	{

	}
}


int main(void)
{
	class MyString ms;
	std::cout << ms.StrCat("test", "cat");
}


