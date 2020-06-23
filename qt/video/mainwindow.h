#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actStartCamera_2_triggered();

    void on_actQuit_triggered();

    void on_actCapture_triggered();

    void on_actCloseCamera_triggered();

private:
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
