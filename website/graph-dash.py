import matplotlib.pyplot as plt
import pandas as pd

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    data = pd.read_csv('website\static\graph.csv')
    df = pd.DataFrame(data)


    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color=['g','r','b','y'])
    plt.title("HYD DC Total Sevice Count")
    plt.xlabel("Devices")
    plt.ylabel("Number of Devices")
    #plt.plot(X,Y)
    for a,b in zip(X, Y): 
        plt.text(a, b, str(b))
    fig = plt.show()
    # Send the graph as a file
    return app.render_template("graph.html", fig=fig )

if __name__ == "__main__":
    app.run()

''' data = pd.read_csv('website\static\graph.csv')
df = pd.DataFrame(data)

X = list(df.iloc[:, 0])
Y = list(df.iloc[:, 1])

# Plot the data using bar() method
plt.bar(X, Y, color=['g','r','b','y'])
plt.title("HYD DC Total Sevice Count")
plt.xlabel("Devices")
plt.ylabel("Number of Devices")
#plt.plot(X,Y)
for a,b in zip(X, Y): 
    plt.text(a, b, str(b))

# Show the plot
plt.show() '''

'''@views.route('/home8')
def home8():
    data = pd.read_csv('website\static\graph.csv')
    df = pd.DataFrame(data)

    img = BytesIO()
    X = list(df.iloc[:, 0])
    Y = list(df.iloc[:, 1])

    # Plot the data using bar() method
    plt.bar(X, Y, color=['g','r','b','y'])
    plt.title("HYD DC Total Sevice Count")
    plt.xlabel("Devices")
    plt.ylabel("Number of Devices")
    #plt.plot(X,Y)
    for a,b in zip(X, Y): 
        plt.text(a, b, str(b))
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return f"<img src='data:image/png;base64,{plot_url}'/>"
    # Send the graph as a file
    #return render_template("graph.html", plot_url=plot_url )'''