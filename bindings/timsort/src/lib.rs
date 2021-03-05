use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn sort_int(mut array: Vec<i32>) -> PyResult<PyObject>{
    let gil = Python::acquire_gil();
    let py = gil.python();
    array.sort();
    Ok(array.to_object(py))
}

#[pyfunction]
fn sort_float(mut array: Vec<f64>) -> PyResult<PyObject>{
    let gil = Python::acquire_gil();
    let py = gil.python();
    array.sort_by(|a, b| a.partial_cmp(b).unwrap());
    Ok(array.to_object(py))
}

#[pyfunction]
fn sort_str(mut array: Vec<String>) -> PyResult<PyObject>{
    let gil = Python::acquire_gil();
    let py = gil.python();
    array.sort();
    Ok(array.to_object(py))
}

#[pymodule]
fn rusty_sorter(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(sort_int))?;
    m.add_wrapped(wrap_pyfunction!(sort_float))?;
    m.add_wrapped(wrap_pyfunction!(sort_str))?;
    Ok(())
}