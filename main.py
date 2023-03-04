def create_relation_dict(net):
    relation_dict = {}
    for item in net:
        name_one = item[0]
        name_two = item[1]
        if name_one not in relation_dict:
            relation_dict[name_one] = []
        if name_two not in relation_dict:
            relation_dict[name_two] = []
        relation_dict[name_one].append(name_two)
        relation_dict[name_two].append(name_one)
    return relation_dict


def check_relation(net, first, second):
    if (first,second) in net or (second,first) in net:
        return True
    relation_dict = create_relation_dict(net)
    visited = {key: False for key in relation_dict.keys()}

    def dfs(curr_vertex):
        visited[curr_vertex] = True
        for vertex in relation_dict[curr_vertex]:
            if not visited[vertex]:
                dfs(vertex)

    dfs(first)
    return visited[second]


if __name__ == '__main__':
    net = (
        ('Ваня', 'Лёша'), ('Лёша', 'Катя'),
        ('Ваня', 'Катя'), ('Вова', 'Катя'),
        ('Лёша', 'Лена'), ('Оля', 'Петя'),
        ('Стёпа', 'Оля'), ('Оля', 'Настя'),
        ('Настя', 'Дима'), ('Дима', 'Маша')
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
