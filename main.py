from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import plotly.graph_objects as go  # рисует продвинутые графики, иногда используется в VDA

if __name__ == '__main__':
    print("Введите число N: ", end=' ')
    n = int(input())
    rec = Rectangle(n, n, 'blue')
    circle = Circle(n, 'green')
    sqr = Square(n, 'red')

    fig = go.Figure()

    # Выставим одинаковый масштаб по всем осям, иначе окружность будет эллипсом, а квадрат - не квадратом
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    # квадрат
    fig.add_shape(type="rect",
                  xref='x', yref='y',
                  x0=3 * n + 2, y0=0, x1=4 * n + 2, y1=n,  # координаты вершин прямоугольника,расположенных по диагонали
                  line=dict(color='red', width=8),
                  fillcolor='coral'
                  )
    # прямоугольник
    fig.add_shape(type="rect",
                  xref='x', yref='y',
                  x0=2*n+1, y0=0, x1=3*n+1, y1=n,  # координаты вершин прямоугольника, расположенных по диагонали
                  line=dict(color='blue', width=5),
                  fillcolor='Royalblue'
                  )
    # окружность
    fig.add_shape(type="circle",
                  xref="x", yref="y",
                  x0=0, y0=0, x1=2*n, y1=2*n,  # координаты вершин квадрата, описанного около окружности
                  line_color="green",
                  )
    fig.add_trace(go.Scatter(
        x=[n, 2.5*n + 1, 3.5*n + 2],
        y=[n, n+.25, n+.25],
        text=["Окружность",
              "Прямоугольник",
              "Квадрат"],
        mode="text",
    ))


    # А ещё можно так
    fig1 = go.Figure(
        go.Scatter(x=[2*n+1, 3*n+1, 3*n+1, 2*n+1, 2*n+1, None, 3*n+2, 4*n+2, 4*n+2, 3*n+2, 3*n+2],
                   y=[0, 0, n, n, 0,  None, 0, 0, n, n, 0],
                   fill="toself"))

    fig1.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    fig1.show()
    fig.show()
