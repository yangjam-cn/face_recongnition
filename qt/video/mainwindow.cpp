#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actStartCamera_2_triggered()
{

}

void MainWindow::on_actQuit_triggered()
{

}

void MainWindow::on_actCapture_triggered()
{

}

void MainWindow::on_actCloseCamera_triggered()
{

}
