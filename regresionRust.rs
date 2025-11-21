use std::time::Instant;

struct RegresionConcurrente {
    w: f64,
    b: f64,
    learning_rate: f64,
    epochs: usize,
    historial_mse: Vec<f64>,
}

impl RegresionConcurrente {
    fn new(learning_rate: f64, epochs: usize) -> Self {
        RegresionConcurrente {
            w: 0.0,
            b: 0.0,
            learning_rate,
            epochs,
            historial_mse: Vec::new(),
        }
    }

    fn calcular_gradientes(&self, x: &[f64], y: &[f64], y_pred: &[f64]) -> (f64, f64) {
        let m = x.len() as f64;
        let mut suma_error_x = 0.0;
        let mut suma_error = 0.0;
        for i in 0..x.len() {
            let error = y_pred[i] - y[i];
            suma_error_x += error * x[i];
            suma_error += error;
        }
        let dw = (2.0 / m) * suma_error_x;
        let db = (2.0 / m) * suma_error;
        (dw, db)
    }

    fn entrenar(&mut self, x: &[f64], y: &[f64]) -> f64 {
        let inicio = Instant::now();
        let m = x.len();

        for epoch in 0..self.epochs {
            let y_pred: Vec<f64> = x.iter().map(|xi| self.w * xi + self.b).collect();

            let (dw, db) = self.calcular_gradientes(x, y, &y_pred);

            self.w -= self.learning_rate * dw;
            self.b -= self.learning_rate * db;

            if (epoch + 1) % 100 == 0 {
                let mse: f64 = y_pred.iter()
                                .zip(y.iter())
                                .map(|(yp, yi)| (yp - yi).powi(2))
                                .sum::<f64>()
                                / m as f64;

                self.historial_mse.push(mse);
                println!(
                    "Marca {}, MSE: {:.6}, w: {:.4}, b: {:.4}",
                    epoch + 1,
                    mse,
                    self.w,
                    self.b
                );
            }
        }

        let duracion = inicio.elapsed().as_secs_f64();
        duracion
    }

    fn predecir(&self, x: f64) -> f64 {
        self.w * x + self.b
    }
}

fn main() {
    let x: Vec<f64> = vec![1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0];
    let y: Vec<f64> = vec![2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0];

    let learning_rate = 0.01;
    let epochs = 1000;

    println!("============================================================");
    println!("Regresión lineal en Rust");
    println!("============================================================");

    let mut modelo_rust = RegresionConcurrente::new(learning_rate, epochs);
    let tiempo_rust = modelo_rust.entrenar(&x, &y);

    println!("\nTiempo total: {:.4} segundos", tiempo_rust);
    println!("w ≈ {:.4}, b ≈ {:.4}", modelo_rust.w, modelo_rust.b);
    println!("Predicción para x=11: {:.4}", modelo_rust.predecir(11.0));
}

