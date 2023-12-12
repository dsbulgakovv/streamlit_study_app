import streamlit as st
import pandas as pd
from PIL import Image


def preload_content():
    """ preload content used in web app """

    data = pd.read_pickle('data/full_table.pkl')
    main_pic = Image.open('content/main.png')
    corr_plot = Image.open('content/corr_plot.png')
    age_dep_hue = Image.open('content/age_dependants_hue.png')
    cred_fp_scat = Image.open('content/credit_fstpay_scatter.png')
    pair_plot = Image.open('content/pair_plot.png')
    four_plots = Image.open('content/four_plots_distrs.png')
    cred_distr = Image.open('content/credit_distr.png')

    return data, main_pic, corr_plot, age_dep_hue,\
        cred_fp_scat, pair_plot, four_plots, cred_distr


def render_page(data, main_pic, corr_plot, age_dep_hue, cred_fp_scat, pair_plot, four_plots, cred_distr):
    """ creates app page with tabs """

    st.title('Банковские клиенты')
    st.subheader('Исследуем данные о клиентах банков, их кредитах и займах')
    st.image(main_pic)

    tab1, tab2 = st.tabs([':mag: Исследовадание', ':mag: Модель'])

    with tab1:
        st.write('Разведочный анализ данных')

        st.write('**Возраст пассажиров**')
        st.image(four_plots)
        st.write('Самый распространённый пол банковских клиентов в выборке - мужской.')
        st.write('Большее количество клиентов имеет персональный доход около 50 000 рублей.')
        st.divider()

        st.write('**Матрица корреляций**')
        st.image(corr_plot)
        st.write('Сильнее всего коррелируют:')
        st.write('- сумма кредита с первым платежом')
        st.write('- сумма кредита со сроком займа')
        st.divider()

        st.write('**Совместные распределения вещественных признаков**')
        st.image(pair_plot)
        st.divider()

        st.write('**Рассеяние для самых скореллированных признаков**')
        st.image(cred_fp_scat)
        st.divider()

        st.write('**Рассеяние для признаков, имеющих наибольшую связь с таргетом**')
        st.image(age_dep_hue)
        st.divider()

        st.write('**Распределение сумм кредитных средств**')
        st.image(cred_distr)
        st.divider()

        with tab2:
            st.write('**Модель в процессе разработки...**')


def load_page():
    """ loads main page """

    data, main_pic, corr_plot, age_dep_hue, \
        cred_fp_scat, pair_plot, four_plots, cred_distr = preload_content()

    st.set_page_config(layout="wide",
                       page_title="Банки __инсайд__",
                       page_icon=':dollar:')

    render_page(data, main_pic, corr_plot, age_dep_hue,
                cred_fp_scat, pair_plot, four_plots, cred_distr)


if __name__ == "__main__":
    load_page()
