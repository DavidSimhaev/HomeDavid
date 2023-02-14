from itertools import groupby
g = [{'color': 'Черный'}, {'color': 'Черный'}]

d = list(map(lambda x: x[0] , groupby(g, key=lambda x: x["color"])  ))
print(d)

for (int i = 0; i < 10; i++)
{
    // Выводим одну строку из 10 звездочек.
    for (int j = 0; j < 10; j++)
    {
        Console.Write("*");
    }

    // Переход на новую строку.
    Console.WriteLine();
}