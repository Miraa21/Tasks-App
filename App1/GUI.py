from Modules import functions
import PySimpleGUI as sg


label= sg.Text("Enter a Task")
input_box= sg.InputText(tooltip="Type task")
add_button=sg.Button("Add")

window= sg.Window("Tasks App", layout=[[label], [input_box,add_button]]) #each elemnt in a square bracket as each bracket is a row
window.read() #when window opens
window.close() #when user action closes window
