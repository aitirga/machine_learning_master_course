from iml.modules.hydrogeology.dataset_generators import AnalyticalWellEvolutionDatasetEngine
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    dataset_generator = AnalyticalWellEvolutionDatasetEngine(
        # well_locations={'well_1': (0, 0), 'well_2': (1, 1)},
        well_locations={'pozo_1': (0, 0),
                        'pozo_2': (100, 100),
                        'pozo_3': (100, 0),

                        },
        well_pumping={'pozo_1': {'min': 1000, 'max': 1500},
                        'pozo_2': {'min': 500, 'max': 2000},\
                        'pozo_3': {'min': 100, 'max': 3000},\
                      },
        t_final=240.0,
        t_pumping_std=15,
        t_pumping_mean=100,
        nt=1000,
        d_charac=1,
        t_charac=1,
        diffusivity=1.0,
        number_of_stress_periods=75,
        cur_off_rate=0.3,
        extreme_recovery_rate=0.0,
    )
    look_position = (50.0, 50.0)
    # result = dataset_generator.compute_timeseries(x=look_position[0], y=look_position[1])
    # Plot the result as a timeseries
    # plt.plot(result)
    # plt.show()
    # print(result.shape)
    # Save result to head file
    # analytical = dataset_generator._analytical_solution_convolution(x=0, y=0)
    timeseries = dataset_generator.compute_timeseries_at_x_y(x=look_position[0], y=look_position[1])
    output_df = pd.DataFrame(timeseries, columns=['nivel'])
    output_df.index.name = 'tiempo'
    fig, ax = plt.subplots()
    ax.plot(timeseries)
    ax.set_xlabel('Tiempo (días)')
    ax.set_ylabel('Nivel (m)')
    plt.show()
    # dataset_generator.plot_input_output_timeseries(x=look_position[0],
    #                                                y=look_position[1],
    #                                                plot_pumpings=False,
    #                                                master_well='well_1',
    #                                                master_diff_factor=5.0,
    #                                                )
    dataset_generator.plot_well_configuration(x=look_position[0], y=look_position[1], save_path='well_configuration.png')

    for well in dataset_generator.well_names:
        well_data = dataset_generator.pump_evolution[well]
        output_df[well] = well_data

    # Save well data
    output_df.to_csv('data.csv')





