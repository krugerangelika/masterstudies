from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from dash import html, dcc



def create_sidebar():
    return html.Div(
        [
            html.H2("Menu", className="display-4"),
            html.Hr(),
            dcc.Store(id='show-add-patient-button', data=False),
            dbc.Nav(
                [
                    # Sekcja Dashboard / Panel główny
                    dbc.NavLink("Panel Główny", href="/main-panel/", id="dashboard-link", active="exact"),

                    # Sekcja Pacjenci
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink(
                                        "Zarejestruj Nowego Pacjenta",
                                        href="/patient-registration/",  # Correct URL here
                                        id="show-add-patient-link",
                                        className="ms-3"
                                    ),
                                    dbc.NavLink("Lista Pacjentów", href="/main-panel/patient-list/", className="ms-3"),
                                    dbc.NavLink("Karty Pacjentów", href="/main-panel/patient-cards/", className="ms-3"),
                                    dbc.NavLink("Przyjęcia i Zwolnienia", href="/main-panel/admissions-discharges/", className="ms-3"),
                                ],
                                title="Pacjenci",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Opieka Medyczna
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zarządzanie Wizytami", href="/main-panel/visit-management/", className="ms-3"),
                                    dbc.NavLink("Procedury Medyczne", href="/main-panel/medical-procedures/", className="ms-3"),
                                    dbc.NavLink("Monitorowanie Pacjentów", href="/main-panel/patient-monitoring/", className="ms-3"),
                                ],
                                title="Opieka Medyczna",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Personel Medyczny
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zarządzanie Pracownikami", href="/main-panel/staff-management/", className="ms-3"),
                                    dbc.NavLink("Grafik Zespołu", href="/main-panel/team-schedule/", className="ms-3"),
                                    dbc.NavLink("Szkolenia i Certyfikaty", href="/main-panel/training-certificates/", className="ms-3"),
                                ],
                                title="Personel Medyczny",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Oddziały Szpitalne
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zarządzanie Oddziałami", href="/main-panel/ward-management/", className="ms-3"),
                                    dbc.NavLink("Raporty Oddziałowe", href="/main-panel/ward-reports/", className="ms-3"),
                                    dbc.NavLink("Przydział Personelu", href="/main-panel/staff-assignment/", className="ms-3"),
                                ],
                                title="Oddziały Szpitalne",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Apteka
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zarządzanie Lekami", href="/main-panel/pharmacy-management/", className="ms-3"),
                                    dbc.NavLink("Historia Zamówień", href="/main-panel/order-history/", className="ms-3"),
                                    dbc.NavLink("Zarządzanie Receptami", href="/main-panel/prescription-management/", className="ms-3"),
                                ],
                                title="Apteka",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Laboratoria
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zarządzanie Badaniami", href="/main-panel/lab-tests-management/", className="ms-3"),
                                    dbc.NavLink("Wyniki Badań", href="/main-panel/lab-results/", className="ms-3"),
                                    dbc.NavLink("Zarządzanie Pracowniami", href="/main-panel/lab-management/", className="ms-3"),
                                ],
                                title="Laboratoria",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Administracja i Rozliczenia
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Faktury i Rozliczenia", href="/main-panel/billing/", className="ms-3"),
                                    dbc.NavLink("Raporty Finansowe", href="/main-panel/financial-reports/", className="ms-3"),
                                    dbc.NavLink("Zarządzanie Umowami", href="/main-panel/contract-management/", className="ms-3"),
                                ],
                                title="Administracja i Rozliczenia",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Zarządzanie Systemem
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Użytkownicy", href="/main-panel/user-management/", className="ms-3"),
                                    dbc.NavLink("Role i Uprawnienia", href="/main-panel/roles-permissions/", className="ms-3"),
                                    dbc.NavLink("Ustawienia Systemowe", href="/main-panel/system-settings/", className="ms-3"),
                                ],
                                title="Zarządzanie Systemem",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Dokumentacja Medyczna
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Przegląd Dokumentacji", href="/main-panel/medical-documents/", className="ms-3"),
                                    dbc.NavLink("Szablony Dokumentów", href="/main-panel/document-templates/", className="ms-3"),
                                    dbc.NavLink("Zgody i Oświadczenia", href="/main-panel/consent-forms/", className="ms-3"),
                                ],
                                title="Dokumentacja Medyczna",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Bezpieczeństwo i Zgłoszenia
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zgłoszenia Zdarzeń", href="/main-panel/incident-reports/", className="ms-3"),
                                    dbc.NavLink("Zarządzanie Ryzykiem", href="/main-panel/risk-management/", className="ms-3"),
                                    dbc.NavLink("Edukacja i Szkolenia", href="/main-panel/safety-training/", className="ms-3"),
                                ],
                                title="Bezpieczeństwo i Zgłoszenia",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Komunikacja
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Wiadomości Wewnętrzne", href="/main-panel/internal-messages/", className="ms-3"),
                                    dbc.NavLink("Powiadomienia i Alerty", href="/main-panel/notifications/", className="ms-3"),
                                    dbc.NavLink("Konsultacje Zdalne", href="/main-panel/remote-consultations/", className="ms-3"),
                                ],
                                title="Komunikacja",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Logistyka i Zarządzanie Zasobami
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zarządzanie Zapasami", href="/main-panel/supply-management/", className="ms-3"),
                                    dbc.NavLink("Zarządzanie Sprzętem", href="/main-panel/equipment-management/", className="ms-3"),
                                    dbc.NavLink("Transport Pacjentów", href="/main-panel/patient-transport/", className="ms-3"),
                                ],
                                title="Logistyka i Zarządzanie Zasobami",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Konsultacje i Interdyscyplinarność
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Konsylia Lekarskie", href="/main-panel/medical-council/", className="ms-3"),
                                    dbc.NavLink("Zespoły Interdyscyplinarne", href="/main-panel/interdisciplinary-teams/", className="ms-3"),
                                ],
                                title="Konsultacje i Interdyscyplinarność",
                            ),
                        ],
                        start_collapsed=True,
                    ),

                    # Sekcja Zgłaszanie i Feedback
                    dbc.Accordion(
                        [
                            dbc.AccordionItem(
                                [
                                    dbc.NavLink("Zgłoszenia Pacjentów", href="/main-panel/patient-feedback/", className="ms-3"),
                                    dbc.NavLink("Ankiety Satysfakcji", href="/main-panel/patient-surveys/", className="ms-3"),
                                    dbc.NavLink("Zarządzanie Jakością", href="/main-panel/quality-management/", className="ms-3"),
                                ],
                                title="Zgłaszanie i Feedback",
                            ),
                        ],
                        start_collapsed=True,
                    ),
                ],
                vertical=True,
                pills=True,
            ),
            dbc.Button("Dodaj Nowego Pacjenta", id="add-patient-button", color="primary", href="/main-panel/patient-registration/", className="ms-3", style={"display": "none"}),
        ],
        style={"position": "fixed", "top": 0, "left": 0, "bottom": 0, "width": "18rem", "padding": "2rem 1rem",
               "backgroundColor": "#f8f9fa"},
    )

def register_sidebar_callbacks(app):
    @app.callback(
        Output('add-patient-button', 'style'),
        [Input('show-add-patient-link', 'n_clicks')],
        [State('show-add-patient-button', 'data')]
    )
    def show_add_patient_button(n_clicks, current_state):
        if n_clicks:
            # Pokazanie przycisku "Dodaj Nowego Pacjenta" po kliknięciu linku
            return {"display": "block"}
        return {"display": "none"}
